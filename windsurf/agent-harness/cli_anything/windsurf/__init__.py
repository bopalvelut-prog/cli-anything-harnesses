import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Windsurf start')
@cli.command()
def models(): click.echo('Windsurf models')
if __name__ == '__main__': cli()
