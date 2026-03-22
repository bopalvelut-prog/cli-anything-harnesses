import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Graphene status')
if __name__ == '__main__': cli()
