import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def play(): click.echo('GraphQL playground')
@cli.command()
def schema(): click.echo('GraphQL schema')
if __name__ == '__main__': cli()
