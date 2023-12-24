interface Props {
  children: JSX.Element;
  skeleton: JSX.Element;
  isLoading: boolean;
}

function ComponentLoader({
  children,
  skeleton,
  isLoading,
}: Props): JSX.Element {
  return isLoading ? skeleton : children;
}

export default ComponentLoader;
