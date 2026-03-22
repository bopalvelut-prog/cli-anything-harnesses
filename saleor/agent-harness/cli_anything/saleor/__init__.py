import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def manage(): subprocess.run(['saleor', 'manage'])
@cli.command()
def graphql(): click.echo('Saleor GraphQL')
if __name__ == '__main__': cli()
