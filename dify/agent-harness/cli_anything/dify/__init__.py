import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Dify chat')
@cli.command()
def apps(): click.echo('Dify apps')
if __name__ == '__main__': cli()
