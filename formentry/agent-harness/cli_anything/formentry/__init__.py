import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('FormEntry forms')
if __name__ == '__main__': cli()
