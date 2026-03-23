import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('common_lisp running')
@cli.command()
def start(): click.echo('common_lisp started')
if __name__ == '__main__': cli()
