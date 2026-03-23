import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lsp running')
@cli.command()
def start(): click.echo('lsp started')
if __name__ == '__main__': cli()
