import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Rspamd running')
@cli.command()
def test(): click.echo('Rspamd test')
if __name__ == '__main__': cli()
