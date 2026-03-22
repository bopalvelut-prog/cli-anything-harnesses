import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def sms(): click.echo('Bird SMS sent')
if __name__ == '__main__': cli()
