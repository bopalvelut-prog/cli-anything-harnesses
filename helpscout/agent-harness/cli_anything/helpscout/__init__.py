import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def conversations(): click.echo('Help Scout conversations')
@cli.command()
def mailboxes(): click.echo('Help Scout mailboxes')
if __name__ == '__main__': cli()
