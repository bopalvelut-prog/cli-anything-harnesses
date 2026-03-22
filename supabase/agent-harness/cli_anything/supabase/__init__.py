import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['supabase', 'start'])
@cli.command()
def stop(): subprocess.run(['supabase', 'stop'])
@cli.command()
def status(): subprocess.run(['supabase', 'status'])
@cli.command()
def db_reset(): subprocess.run(['supabase', 'db', 'reset'])
if __name__ == '__main__': cli()
